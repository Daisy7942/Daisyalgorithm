function solution(n, k) {
    const lambPrice = 12000;
    const drinkPrice = 2000;
    const freeDrinks = Math.floor(n / 10);
    //  먹은 음료수 k에 무료 음료수가 함께 포함되어 있음
    // 먹은 음료수 k- freeDrinks  = 사는 음료수
    const paidDrinks = k - freeDrinks;
    const answer= (n* lambPrice)+(paidDrinks*drinkPrice);
    return answer;
}

