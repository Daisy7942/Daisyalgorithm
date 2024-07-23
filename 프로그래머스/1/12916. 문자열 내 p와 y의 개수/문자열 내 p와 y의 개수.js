function solution(s){
    let pCount =0;
    for(let i= 0; i<=s.length; i++) {
       if( s[i] == "p" | s[i] == "P" ) {
           pCount += 1 
       }
    }
        
    let yCount =0;
    for(let i= 0; i<=s.length; i++) {
       if( s[i] == "y" | s[i] == "Y" ) {
           yCount += 1 
       }
    }
    if(pCount==yCount){
        return true;
    }else{
        return false;
    }

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('Hello Javascript')

    return answer;
}
