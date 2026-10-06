#!/usr/bin/env python3
"""
Large Memory Substring Benchmark
Allocates multi-gigabyte strings (up to ~8.5-9 GB) and tests substring search
while monitoring live RAM and Swap usage.
"""

import sys
import time
import psutil
import argparse


def print_memory_status(label: str):
    vm = psutil.virtual_memory()
    sw = psutil.swap_memory()
    print(f"\n--- {label} ---")
    print(f"  Physical RAM Used : {vm.used / (1024**3):.2f} GB / {vm.total / (1024**3):.2f} GB ({vm.percent}%)")
    print(f"  Physical RAM Free : {vm.available / (1024**3):.2f} GB")
    print(f"  Swap Used         : {sw.used / (1024**3):.2f} GB / {sw.total / (1024**3):.2f} GB ({sw.percent}%)")


def main():
    parser = argparse.ArgumentParser(description="Test multi-gigabyte memory substring search.")
    parser.add_argument("--gb", type=float, default=8.5, help="Target string memory in GB (default: 8.5)")
    parser.add_argument("--sub", type=str, default="CDC", help="Target substring (default: CDC)")
    parser.add_argument("--matches", type=int, default=10, help="Number of matches to embed (default: 10)")
    parser.add_argument("--allow-slicing", action="store_true", help="Try slicing algorithm (WARNING: requires 2x RAM!)")
    args = parser.parse_args()

    target_bytes = int(args.gb * 1_000_000_000)
    print("=" * 65)
    print(f" MULTI-GIGABYTE MEMORY BENCHMARK ({args.gb} GB)")
    print("=" * 65)

    print_memory_status("Memory BEFORE Allocation")

    print(f"\nAllocating {target_bytes:,} characters (~{args.gb:.2f} GB) in RAM...")
    t0 = time.perf_counter()

    # Build repeating pattern with target substring
    block_size = target_bytes // args.matches
    filler = "A" * (block_size - len(args.sub))
    block = filler + args.sub
    big_string = block * args.matches

    # Fill remainder
    rem = target_bytes - len(big_string)
    if rem > 0:
        big_string += "A" * rem

    alloc_time = time.perf_counter() - t0
    actual_gb = sys.getsizeof(big_string) / (1024**3)

    print(f"Allocated successfully in {alloc_time:.2f} seconds!")
    print(f"Exact string memory footprint: {actual_gb:.2f} GB")

    print_memory_status("Memory AFTER Allocating String")

    # 1. Pointer search (O(1) memory overhead)
    print("\n" + "=" * 65)
    print("Running Pointer Search (str.find - No duplicate memory)")
    print("=" * 65)
    t1 = time.perf_counter()
    count = 0
    start = 0
    while True:
        idx = big_string.find(args.sub, start)
        if idx == -1:
            break
        count += 1
        start = idx + 1
    pointer_time = time.perf_counter() - t1

    print(f"Matches found: {count} (Expected: {args.matches})")
    print(f"Search time:   {pointer_time:.4f} seconds")
    print(f"Status:        {'PASSED' if count == args.matches else 'FAILED'}")

    # 2. Slicing algorithm (optional warning)
    if args.allow_slicing:
        print("\n" + "=" * 65)
        print("WARNING: Running Original Slicing Algorithm...")
        print("This will attempt to allocate a SECOND string of the same size!")
        print("=" * 65)
        try:
            s_copy = big_string
            t2 = time.perf_counter()
            s_count = 0
            first = args.sub[0]
            while True:
                idx = s_copy.index(first)
                word = s_copy[idx : idx + len(args.sub)]
                if word == args.sub:
                    s_count += 1
                s_copy = s_copy[idx + 1 :]
            s_time = time.perf_counter() - t2
            print(f"Slicing matches: {s_count} in {s_time:.2f} seconds")
        except MemoryError:
            print("MemoryError! Slicing failed because system ran out of RAM for the 2nd copy.")
    else:
        print("\n[NOTE] Slicing was skipped because duplicating an 8.5 GB string requires 17 GB of RAM.")
        print("       Use --allow-slicing only on smaller sizes (e.g. --gb 2 --allow-slicing).")

    print("\n" + "=" * 65)
    print("Cleaning up memory...")
    del big_string
    print_memory_status("Memory AFTER Freeing String")
    print("=" * 65)


if __name__ == "__main__":
    main()
