function solution(quiz) {
    var answer = [];
    
    for (let i = 0; i<quiz.length; i++) {
        let arr = quiz[i].split(" ");
        let result = 0;
        console.log(arr)
        
        if (arr[1] == "-") {
            result = Number(arr[0])-Number(arr[2])
        } else {
            result = Number(arr[0])+Number(arr[2])
        }
        
        console.log(result)
        
        if (result == Number(arr[4])) {
            answer.push("O")
        } else {
            answer.push("X")
        }
    }
    return answer;
}