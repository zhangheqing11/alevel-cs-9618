#!/usr/bin/env python3
"""Run six reference/alternate candidates and targeted audit counterexamples.

Uses make try in disposable attempts folders, deleting only folders this run
created. Existing attempts cause an error instead of being overwritten.
"""
import ast
import json
from pathlib import Path
import re
import shutil
import subprocess
from check_handbook import ROOT

EXERCISES=['9618_s24_42_q3','9618_w25_43_q3','9618_s25_42_q1',
           '9618_w24_41_q3','9618_s24_41_q2','9618_w25_42_q1']


class WhileVariant(ast.NodeTransformer):
    """Use while for a range loop with no loop-control statements or target writes."""
    changed=False
    def visit_For(self,node):
        if self.changed:return node
        if not (isinstance(node.target,ast.Name) and isinstance(node.iter,ast.Call)
                and isinstance(node.iter.func,ast.Name) and node.iter.func.id=='range'
                and 1<=len(node.iter.args)<=2 and not node.orelse):return self.generic_visit(node)
        if any(isinstance(n,(ast.Break,ast.Continue)) or
               (isinstance(n,ast.Name) and isinstance(n.ctx,ast.Store) and n.id==node.target.id)
               for b in node.body for n in ast.walk(b)):return self.generic_visit(node)
        self.changed=True
        self.selected=node
        start=ast.Constant(0) if len(node.iter.args)==1 else node.iter.args[0]
        end=node.iter.args[-1]
        return [ast.Assign(targets=[node.target],value=start),
                ast.Assign(targets=[ast.Name(id='_audit_stop',ctx=ast.Store())],value=end),
                ast.While(test=ast.Compare(left=ast.Name(id=node.target.id,ctx=ast.Load()),
                    ops=[ast.Lt()],comparators=[ast.Name(id='_audit_stop',ctx=ast.Load())]),
                    body=node.body+[ast.AugAssign(target=node.target,op=ast.Add(),value=ast.Constant(1))],orelse=[])]


def alternate(code):
    transformer=WhileVariant();tree=transformer.visit(ast.parse(code))
    if transformer.changed:
        node=transformer.selected
        lines=code.splitlines(keepends=True)
        indent=' ' * node.col_offset
        start='0' if len(node.iter.args)==1 else ast.unparse(node.iter.args[0])
        end=ast.unparse(node.iter.args[-1])
        # Preserve original comments, including all required type declarations.
        replacement=[indent+'_audit_start = '+start+'\n',indent+'_audit_stop = '+end+'\n',
            indent+node.target.id+' = _audit_start\n',
            indent+'while '+node.target.id+' < _audit_stop:\n']
        replacement+=lines[node.lineno:node.end_lineno]
        replacement+=[indent+'    '+node.target.id+' += 1\n']
        return ''.join(lines[:node.lineno-1]+replacement+lines[node.end_lineno:])
    # A local file-loop name is not part of the callable interface.
    return re.sub(r'\bLine\b','InputLine',code)


def replace_main(code,body):
    tree=ast.parse(code)
    for node in tree.body:
        if isinstance(node,ast.If) and '__name__' in ast.unparse(node.test):
            node.body=ast.parse(body).body
    return ast.unparse(ast.fix_missing_locations(tree))+'\n'


def cases(name,code):
    yield 'reference',code
    yield 'alternate',alternate(code)
    if name=='9618_s24_42_q3':
        yield 'valid_numeric_label',code.replace('    # NumberArray:', '    print("Question 3")\n    # NumberArray:')
    if name=='9618_s25_42_q1':
        yield 'invalid_main_no_calls',replace_main(code,
            'FileName = input("Filename: ")\nif FileName == "StackData.txt":\n    print(131)\nelse:\n    print(320)')
    if name=='9618_w24_41_q3':
        yield 'invalid_main_no_calls',replace_main(code,'''Data = []
for AuditIndex in range(5):
    Data.append(int(input("Enter: ")))
for AuditIndex in range(4, -1, -1):
    print(Data[AuditIndex])
print("After")
Skipped = False
for AuditIndex in range(4, -1, -1):
    if Data[AuditIndex] == 5 and not Skipped:
        Skipped = True
    else:
        print(Data[AuditIndex])
''')
    if name=='9618_s24_41_q2':
        # Same nine Tree objects in the first nine positions, spare capacity after.
        capacity=code.replace('return TreeObjects','return TreeObjects + [None] * 11')
        capacity=capacity.replace('    for Item in Trees:\n', '    for Item in Trees:\n        if Item is None:\n            continue\n')
        yield 'valid_capacity_20',capacity
    if name=='9618_w25_42_q1':
        yield 'valid_multiline_message',re.sub(
            r"print\((FirstBird|SecondBird)\.GetSpecies\(\), 'is currently at', \1\.GetPosition\(\)\)",
            r"print(\1.GetSpecies(), 'is currently at'); print(\1.GetPosition())",code)


def main():
    results=[]
    for name in EXERCISES:
        ex=ROOT/'practice/p4'/name
        attempt=ROOT/'attempts/practice/p4'/name
        if attempt.exists():raise RuntimeError(f'Refuse to overwrite {attempt}')
        code=(ex/'ref/solution.py').read_text()
        try:
            attempt.mkdir(parents=True)
            for label,candidate in cases(name,code):
                (attempt/'solution.py').write_text(candidate)
                p=subprocess.run(['make','try','EX=practice/p4/'+name],cwd=ROOT,
                    text=True,capture_output=True,timeout=60)
                result=dict(exercise=name,case=label,exit_code=p.returncode,
                    summary=p.stdout.splitlines()[-1] if p.stdout.splitlines() else '',
                    stdout=p.stdout,stderr=p.stderr)
                results.append(result)
                print(name,label,p.returncode,result['summary'],flush=True)
        finally:
            shutil.rmtree(attempt)
    out=ROOT/'papers/p4/audit/practice-runs.json'
    out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')


if __name__=='__main__':main()
