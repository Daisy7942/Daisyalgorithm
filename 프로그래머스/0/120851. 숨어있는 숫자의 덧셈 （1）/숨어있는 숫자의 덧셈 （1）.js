function solution(my_string) {
    var answer = 0;
// let number=[1,2,3,4,5,6,7,8,9]
let number = "123456789".split("")
for (let i =0; i<my_string.length; i++){
    if (number.includes(my_string[i])){
    answer += Number(my_string[i])        
    }
}
    return answer;
}