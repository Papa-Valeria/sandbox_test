import { isEven } from "./math";

describe("isEven", () => {
    test("returns true for even numbers", () => {
        expect(isEven(4)).toBe(true);
    });

    test("returns false for odd numbers", () => {
        expect(isEven(5)).toBe(false);
    });

    test("handles zero", () => {
        expect(isEven(0)).toBe(true);
    });

    test("handles negative numbers", () => {
        expect(isEven(-2)).toBe(true);
    });
});