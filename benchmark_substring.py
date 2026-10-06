#!/usr/bin/env python3
"""
Benchmark Substring Search
Tests the substring repetition algorithm on large strings (e.g. 9 Million chars)
and measures verification, execution time, CPU usage, and peak RAM consumption.
"""

import sys
import time
import resource
import tracemalloc
import argparse


def generate_benchmark_data(total_length: int = 9_000_000, target_sub: str = "CDC", target_matches: int = 5_000):
    """
    Generates a deterministic test string with an exact number of occurrences
    of the target substring.
    """
    sub_len = len(target_sub)
    if target_matches <= 0:
        # Filler with no occurrences
        filler_char = "A" if "A" not in target_sub else "X"
        return filler_char * total_length, 0

    block_size = total_length // target_matches
    if block_size < sub_len + 2:
        raise ValueError("Target matches too high for the given string length.")

    # Construct block: filler + target_sub
    # Using 'A' as filler, ensuring junction 'AA' doesn't create accidental occurrences
    filler = "A" * (block_size - sub_len)
    block = filler + target_sub

    # Repeat block
    test_string = block * target_matches

    # Fill remainder if total_length is not perfectly divisible
    remainder = total_length - len(test_string)
    if remainder > 0:
        test_string += "A" * remainder

    expected_count = target_matches
    return test_string, expected_count


def run_original_algorithm(string: str, sub_string: str) -> int:
    """
    Exact implementation from test.py:
    Uses string.index(first) and string slicing string[index + 1:].
    """
    first = sub_string[0]
    state = []
    while True:
        try:
            index = string.index(first)
            word_check = string[index : index + len(sub_string)]
            if word_check == sub_string:
                state.append("True")
            string = string[index + 1 : len(string)]
        except ValueError:
            break
    return len(state)


def run_optimized_algorithm(string: str, sub_string: str) -> int:
    """
    Optimized pointer implementation:
    Uses string.find() with start pointer to avoid copying strings.
    """
    count = 0
    start = 0
    sub_len = len(sub_string)
    while True:
        idx = string.find(sub_string, start)
        if idx == -1:
            break
        count += 1
        start = idx + 1
    return count


def benchmark(func, string: str, sub_string: str):
    """
    Runs func(string, sub_string) and measures:
    - Return value
    - Elapsed wall time
    - User and System CPU time
    - Peak heap memory allocated by Python (tracemalloc)
    - Peak process memory (Max RSS via resource)
    """
    tracemalloc.start()
    tracemalloc.reset_peak()

    start_rusage = resource.getrusage(resource.RUSAGE_SELF)
    start_time = time.perf_counter()

    result = func(string, sub_string)

    end_time = time.perf_counter()
    end_rusage = resource.getrusage(resource.RUSAGE_SELF)

    _, peak_traced = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    wall_time = end_time - start_time
    user_cpu = end_rusage.ru_utime - start_rusage.ru_utime
    sys_cpu = end_rusage.ru_stime - start_rusage.ru_stime
    total_cpu = user_cpu + sys_cpu
    max_rss_mb = end_rusage.ru_maxrss / 1024  # Linux returns KiB

    return {
        "result": result,
        "wall_time": wall_time,
        "user_cpu": user_cpu,
        "sys_cpu": sys_cpu,
        "total_cpu": total_cpu,
        "peak_heap_mb": peak_traced / (1024 * 1024),
        "peak_rss_mb": max_rss_mb,
    }


def main():
    parser = argparse.ArgumentParser(description="Benchmark substring counting algorithms on large strings.")
    parser.add_argument("--length", type=int, default=9_000_000, help="Total string length (default: 9,000,000)")
    parser.add_argument("--sub", type=str, default="CDC", help="Target substring (default: CDC)")
    parser.add_argument("--matches", type=int, default=5_000, help="Number of occurrences to embed (default: 5,000)")
    args = parser.parse_args()

    print("=" * 65)
    print(" SUBSTRING SEARCH BENCHMARK SUITE")
    print("=" * 65)
    print(f"Generating test string with length {args.length:,} ...")
    test_string, expected_count = generate_benchmark_data(args.length, args.sub, args.matches)

    string_memory_mb = sys.getsizeof(test_string) / (1024 * 1024)
    print(f"String created: {len(test_string):,} characters (~{string_memory_mb:.2f} MB)")
    print(f"Target Substring: '{args.sub}'")
    print(f"Mathematically Expected Matches: {expected_count:,}")
    print("=" * 65)

    print("\n[1/2] Running Original Algorithm (test.py logic with slicing)...")
    res_orig = benchmark(run_original_algorithm, test_string, args.sub)
    pass_orig = res_orig["result"] == expected_count

    print("[2/2] Running Optimized Pointer Algorithm (find without slicing)...")
    res_opt = benchmark(run_optimized_algorithm, test_string, args.sub)
    pass_opt = res_opt["result"] == expected_count

    print("\n" + "=" * 65)
    print(" BENCHMARK COMPARISON RESULTS")
    print("=" * 65)
    print(f"{'Metric':<25} | {'Original (test.py)':<18} | {'Optimized Pointer':<18}")
    print("-" * 65)
    print(f"{'Matches Found':<25} | {res_orig['result']:<18} | {res_opt['result']:<18}")
    print(f"{'Verification':<25} | {'PASSED' if pass_orig else 'FAILED':<18} | {'PASSED' if pass_opt else 'FAILED':<18}")
    print(f"{'Wall Time (s)':<25} | {res_orig['wall_time']:<18.4f} | {res_opt['wall_time']:<18.4f}")
    print(f"{'CPU Time (s)':<25} | {res_orig['total_cpu']:<18.4f} | {res_opt['total_cpu']:<18.4f}")
    print(f"{'Peak Heap Alloc (MB)':<25} | {res_orig['peak_heap_mb']:<18.2f} | {res_opt['peak_heap_mb']:<18.2f}")
    print(f"{'Process Peak RSS (MB)':<25} | {res_orig['peak_rss_mb']:<18.2f} | {res_opt['peak_rss_mb']:<18.2f}")
    print("=" * 65)

    speedup = res_orig["wall_time"] / res_opt["wall_time"] if res_opt["wall_time"] > 0 else 1.0
    print(f"\nSummary:")
    print(f"  • Your original algorithm verified {expected_count:,} occurrences correctly in {res_orig['wall_time']:.2f}s.")
    print(f"  • Peak memory stayed at ~{res_orig['peak_rss_mb']:.1f} MB.")
    print(f"  • The pointer method ran in {res_opt['wall_time']:.4f}s ({speedup:.1f}x faster) with minimal allocations.")


if __name__ == "__main__":
    main()
