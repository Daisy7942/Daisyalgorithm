function solution(numbers) {
    const sum= numbers.reduce((acc,curr)=> acc+ curr,0);
    const average = sum / numbers.length;
    if(average% 1 === 0 || average % 1 ===0.5){}
    return average;
}