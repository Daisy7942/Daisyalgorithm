function solution(price) {
    let dcPrice = price;
    if(price>=100000&&price<300000){
        dcPrice = price-price*(5/100)
    }else if(price>=300000&& price<500000){
        dcPrice = price-price*(10/100)
    }else if(price>=500000){
        dcPrice = price-price*(20/100)
    }
    return Math.floor(dcPrice);
}