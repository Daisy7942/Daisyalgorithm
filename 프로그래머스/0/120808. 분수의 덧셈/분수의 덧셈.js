function solution(numer1, denom1, numer2, denom2) {
    // 두 분수의 덧셈
    let newNumer = numer1 * denom2 + numer2 * denom1;
    let newDenom = denom1 * denom2;
    
    // 분자와 분모의 최대공약수 구하기
    let gcdValue = gcd(newNumer, newDenom);
    
    // 기약 분수로 나타내기
    let simplifiedNumer = newNumer / gcdValue;
    let simplifiedDenom = newDenom / gcdValue;
    
    return [simplifiedNumer, simplifiedDenom];
}

function gcd(a, b) {
    // 유클리드 호제법을 사용하여 최대공약수 구하기
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}