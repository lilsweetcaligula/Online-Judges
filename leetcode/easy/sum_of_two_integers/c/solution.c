/*
 * In order to solve this problem in a language like C, we have
 * to resort to bitwise trickery. I admit, I have not figured it
 * out myself, but found it somewhere in the depth of the web.
 * So I may not take credit. I will, however, explain how it
 * works.
 *
 * On each iteration or, in our situation, recursive call, our
 * "raw" sum (that is the addition which does not account for
 * carry at this point) can be imitated by the XOR operation.
 *
 * For example: 8 + 7 = 15
 * In binary:   1000(2) + 111(2) = 1111(2)
 * The same as: 1000(2) ^ 111(2) = 1111(2)
 *
 * However, what happens when we do, in fact, have a carry?
 *
 * For example: 8 + 8 = 16
 * In binary:   1000(2) + 1000(2) = 10000(2)
 * XOR:         1000(2) ^ 1000(2) = 0(2)
 *
 * It is important to point out, however, that the zero result
 * will only happen if both operands (in our case both are equal
 * to 8) are equal. This is one of the tricks compilers use to
 * zero out their registers but I digress.
 *
 * So what do we do now? Well, turns out, we can "capture" the
 * carry by the AND operation. It works because when two "1" bits
 * are added together, a carry occurs. And what can accurately 
 * report we have a carry? That's right - the AND operator.
 * 
 * For example, given that both operands are equal to 8, there we
 * have our carries:
 *
 * AND:         1000(2) & 1000(2) = 1000(2)
 *
 * But carry has to be applied to the consequent bits, not the
 * current one, no problem, we shift the "carry map" to the left
 * 1 position.
 *
 * LSH:         1000(2) << 1 = 10000(2)
 *
 * Now on the next recursive call, we apply the carry map on the XOR
 * product and rinse, repeat until we no longer have a carry, or
 * in other words, until carry is equal to zero.
 *
 * This will not, however, work with negative numbers in languages 
 * with dynamic int types, which can grow indefinitely, such as Python.
 * This is because the sign bit will never be "reached" by the product
 * of the XOR operator, resulting in an infinite loop.
 */

int getSum(int a, int b) 
{
    if (b == 0) {
        return a;
    }
    
    const int sum   = a ^ b;
    const int carry = (a & b) << 1;
    
    return getSum(sum, carry);
}
