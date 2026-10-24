"""Tests for 9618_w22_42 Question 1 (job priority queue in a global 2D array, insertion sort).

Mark point numbers are corpus markpoints[].n (they match the MS bullets here).
"""
import re

from testkit import output_lines, run_script

JOB_LINE = re.compile(r"(?<!\d)(-?\d+)\s+priority\s+(-?\d+)(?!\d)")
GIVEN_JOBS = [(12, 10), (526, 9), (33, 8), (12, 9), (78, 1)]  # QP 1(d) table, in order


def rows(jobs):
    """The array as a list of [job, priority] pairs (works for nested lists or tuples)."""
    return [list(r) for r in jobs]


def job_lines(text):
    """(job, priority) pairs from lines shaped like '123 priority 1'."""
    return [(int(m.group(1)), int(m.group(2))) for m in map(JOB_LINE.search, output_lines(text)) if m]


def fresh(sol, capsys, jobs=GIVEN_JOBS):
    sol.Initialise()
    for job, priority in jobs:
        sol.AddJob(job, priority)
    capsys.readouterr()


def in_priority_order(pairs):
    """Sorted by priority; jobs with equal priority may be in either order (MS: 526 and 12 can be reversed)."""
    return [p for _, p in pairs] == sorted(p for _, p in pairs)


# ---------------------------------------------------------------- 1(a)

def test_1a_jobs_is_100_by_2_and_numberofjobs_declared(sol):
    """9618_w22_42:1(a) MP1-MP3: global 2D array Jobs, 100 x 2; global NumberOfJobs (D10 ①: a real list)."""
    assert isinstance(sol.Jobs, list), "Jobs must be a real list (array), not just a comment"
    assert len(sol.Jobs) == 100
    assert all(len(r) == 2 for r in sol.Jobs)
    assert hasattr(sol, "NumberOfJobs"), "global NumberOfJobs is not declared"


# ---------------------------------------------------------------- 1(b)

def test_1b_initialise_sets_all_minus_one_and_zero(sol):
    """9618_w22_42:1(b) MP1-MP3: every element of both dimensions is -1, NumberOfJobs is 0."""
    sol.NumberOfJobs = 7
    sol.Initialise()
    assert len(sol.Jobs) == 100
    assert rows(sol.Jobs) == [[-1, -1]] * 100
    assert sol.NumberOfJobs == 0


# ---------------------------------------------------------------- 1(c)

def test_1c_addjob_stores_in_next_free_element(sol, capsys):
    """9618_w22_42:1(c) MP4-MP6: job number and priority go to the next free row; NumberOfJobs + 1; 'Added'."""
    sol.Initialise()
    sol.AddJob(12, 10)
    sol.AddJob(526, 9)
    out = output_lines(capsys.readouterr().out)
    assert rows(sol.Jobs[:3]) == [[12, 10], [526, 9], [-1, -1]]
    assert sol.NumberOfJobs == 2
    assert [line for line in out if line in ("Added", "Not added")] == ["Added", "Added"]


def test_1c_addjob_full_outputs_not_added(sol, capsys):
    """9618_w22_42:1(c) MP2-MP3: when 100 jobs are stored, 'Not added' and nothing changes."""
    sol.Initialise()
    for n in range(99):
        sol.AddJob(n + 1, 5)
    capsys.readouterr()
    sol.AddJob(500, 1)  # the 100th job still fits
    assert "Added" in output_lines(capsys.readouterr().out)
    before = rows(sol.Jobs)
    sol.AddJob(777, 2)
    assert "Not added" in output_lines(capsys.readouterr().out)
    assert rows(sol.Jobs) == before
    assert sol.NumberOfJobs == 100


# ---------------------------------------------------------------- 1(e)

def test_1e_insertionsort_orders_given_jobs_by_priority(sol, capsys):
    """9618_w22_42:1(e) MP2-MP5: the 5 jobs end up in ascending priority; whole rows move together."""
    fresh(sol, capsys)
    sol.InsertionSort()
    first5 = [tuple(r) for r in sol.Jobs[:5]]
    assert sorted(first5) == sorted(GIVEN_JOBS), "job numbers and priorities must move together"
    assert in_priority_order(first5)
    assert first5[0] == (78, 1) and first5[1] == (33, 8) and first5[4] == (12, 10)


def test_1e_insertionsort_only_sorts_stored_jobs(sol, capsys):
    """9618_w22_42:1(e) MP2: the outer loop runs over the number of jobs, so unused -1 rows stay at the end."""
    fresh(sol, capsys)
    sol.InsertionSort()
    assert rows(sol.Jobs[5:]) == [[-1, -1]] * 95
    assert sol.NumberOfJobs == 5


def test_1e_insertionsort_reverse_order(sol, capsys):
    """9618_w22_42:1(e) MP3-MP5: priorities 10..1 are fully reversed (inner loop shifts every row up)."""
    fresh(sol, capsys, [(100 + p, p) for p in range(10, 0, -1)])
    sol.InsertionSort()
    assert [tuple(r) for r in sol.Jobs[:10]] == [(100 + p, p) for p in range(1, 11)]


# ---------------------------------------------------------------- 1(f)

def test_1f_printarray_format(sol, capsys):
    """9618_w22_42:1(f) MP1-MP3: one line per stored job, 'priority' between job number and priority."""
    fresh(sol, capsys, [(123, 1), (39, 3), (120, 7)])
    sol.PrintArray()
    assert job_lines(capsys.readouterr().out) == [(123, 1), (39, 3), (120, 7)]


# ---------------------------------------------------------------- 1(d), 1(g)

def test_1g_screenshot_added_five_times_then_jobs_in_order(candidate_path):
    """9618_w22_42:1(g)(ii) MP-03 (also 1(d) MP1-MP2, 1(g)(i)): 'Added' x5, then the jobs in priority order."""
    result = run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    lines = result.lines
    assert sum(line.strip() == "Added" for line in lines) == 5
    jobs = job_lines(result.stdout)
    assert sorted(jobs) == sorted(GIVEN_JOBS), "all five given jobs must be printed once"
    assert in_priority_order(jobs)
    last_added = max(i for i, line in enumerate(lines) if line.strip() == "Added")
    assert job_lines("\n".join(lines[last_added + 1:])) == jobs


def test_1d_1gi_traced_main(candidate_path):
    """9618_w22_42:1(d) MP1–2; 1(g)(i) whole; MS pp.6,9."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path)
    assert r.error is None
    positions = {id(call): index for index, call in enumerate(r.calls)}
    initial, adds, sorts, prints = r.called("Initialise"), r.called("AddJob"), r.called("InsertionSort"), r.called("PrintArray")
    assert initial and sorts and prints
    assert [tuple(c.args.values()) for c in adds] == GIVEN_JOBS
    assert positions[id(initial[0])] < positions[id(adds[0])] < positions[id(adds[-1])] < positions[id(sorts[0])] < positions[id(prints[0])]
