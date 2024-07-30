function solution(my_string) {
    let answer = "";
    let new_my_string = my_string.split("")
    for(let i=0; i<new_my_string.length; i++){
        // if(new_my_string[i].includes(["a","e","i","o","u"])) 
        if(!["a","e","i","o","u"].includes(new_my_string[i])){
            
         answer += new_my_string[i] 
        }
    }
    
    
    return answer;
    
    // "" '' `bcd` "a" ""   "b""c""d"
}