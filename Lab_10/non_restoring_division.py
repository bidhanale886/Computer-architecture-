
    """Lab 10: unsigned binary division using the non-restoring algorithm."""

    from __future__ import annotations

    import argparse


    def bits(value: int, width: int) -> str:
        """Return the low *width* bits of value as a two's-complement bit string."""
        return format(value & ((1 << width) - 1), f"0{width}b")


    def non_restoring_division(dividend: int, divisor: int, *, show_steps: bool = True) -> tuple[int, int]:
        """Divide two non-negative integers and return ``(quotient, remainder)``.

        ``A`` is maintained as a signed (n + 1)-bit partial remainder.  ``Q`` is
        the n-bit quotient register, initially containing the dividend.
        """
        if dividend < 0 or divisor < 0:
            raise ValueError("This implementation accepts unsigned (non-negative) integers only.")
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        n = max(1, dividend.bit_length(), divisor.bit_length())
        a_width = n + 1
        a = 0
        q = dividend
        m = divisor

        if show_steps:
            print(f"Bit width (n): {n}")
            print(f"Initial values: A={bits(a, a_width)}  Q={bits(q, n)}  M={bits(m, a_width)}")
            print("-" * 72)
            print(f"{'Step':<6}{'After shift [A,Q]':<30}{'Operation':<20}{'A':<12}Q")

        for step in range(1, n + 1):
            # Logical left shift of the combined [A, Q] register.
            incoming_bit = (q >> (n - 1)) & 1
            a = (a << 1) | incoming_bit
            q = (q << 1) & ((1 << n) - 1)

            shifted = f"{bits(a, a_width)} {bits(q, n)}"
            if a >= 0:
                a -= m
                operation = "A = A - M"
            else:
                a += m
                operation = "A = A + M"

            if a >= 0:
                q |= 1

            if show_steps:
                print(f"{step:<6}{shifted:<30}{operation:<20}{bits(a, a_width):<12}{bits(q, n)}")

        if a < 0:
            if show_steps:
                print("Final correction: A is negative, so A = A + M")
            a += m

        if show_steps:
            print("-" * 72)
            print(f"Quotient:  {bits(q, n)} (decimal {q})")
            print(f"Remainder: {bits(a, a_width)} (decimal {a})")

        return q, a


    def run_self_test() -> None:
        """Verify the algorithm against Python's integer division."""
        cases = [(13, 3), (7, 2), (15, 4), (0, 5), (31, 1), (37, 6)]
        for dividend, divisor in cases:
            quotient, remainder = non_restoring_division(dividend, divisor, show_steps=False)
            assert (quotient, remainder) == divmod(dividend, divisor)
        print(f"Passed {len(cases)} non-restoring division test cases.")


    def main() -> None:
        parser = argparse.ArgumentParser(description="Non-restoring division for unsigned integers")
        parser.add_argument("dividend", nargs="?", type=int, help="non-negative dividend")
        parser.add_argument("divisor", nargs="?", type=int, help="positive divisor")
        parser.add_argument("--test", action="store_true", help="run built-in verification tests")
        args = parser.parse_args()

        if args.test:
            run_self_test()
            return

        try:
            dividend = args.dividend if args.dividend is not None else int(input("Enter dividend (decimal): "))
            divisor = args.divisor if args.divisor is not None else int(input("Enter divisor (decimal): "))
            non_restoring_division(dividend, divisor)
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")


    if __name__ == "__main__":
        main()
