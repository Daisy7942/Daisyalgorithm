function solution(money) {
    let coffee = 5500
    let cupCount = Math.floor(money/coffee);
    let remainMoney = money%coffee;
    var answer = [cupCount,remainMoney];
    return answer;
}


 
// 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와
 
// 남는 돈을 순서대로 담은 배열을 return 하도록
// solution 함수를 완성해보세요.