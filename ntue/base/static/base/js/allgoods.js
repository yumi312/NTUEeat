let goods_arr=[];
var json_arr;
var num = 1 ;
let photourl = ['https://www.ihergo.com/photo/product/11/750_11_1555762294225.jpg','https://www.ihergo.com/photo/product/68/750_97768_1657175280011.jpg','https://www.ihergo.com/photo/product/11/750_11_1627531452747.jpg','https://www.ihergo.com/photo/product/11/750_11_1588927840254.jpg'];




//購物車顯示cookie===============================================================
$('.shopcar_btn').click(function(){
    $('.have').text(""); //清空購物車


    var inputString = document.cookie;
    var count = (inputString.match(/=/g) || []).length; //算有幾個=符號
    console.log(count);

    if (count == 0){
        $('.have').text("購物車尚無商品!");
    }


    let text_arr=[]; 
    for (let i=1;i<=count;i++){ //取key
        var tesst = document.cookie.split("{")[i].split("}")[0];
    
        for (let i=1 ; i<=5 ; i++){ //取值
            var text_count = tesst.split(":")[i].split(",")[0];
            console.log(text_count);
            text_arr.push(text_count);
    }
    
}
console.log (text_arr);

    var key_arr1=[];
    var key_arr2=[];
    var ac = text_arr.length;
    for (let x=0 ; x<=((ac/5)-1); x++){

        var key = (text_arr[(0+5*x)] + text_arr[(2+5*x)] );
        k1 = key.replace(/"/g, "");
        key_arr1.push(k1);
        k2 = k1.replace(/%/g, "");
        key_arr2.push(k2);

    

        sci = shopcar_item(key_arr2[x],photourl[0],unescape(text_arr[(1+5*x)]),unescape(text_arr[(2+5*x)]),text_arr[(3+5*x)],text_arr[(4+5*x)],(text_arr[(3+5*x)] * text_arr[(4+5*x)]));
        $('.have').append(sci);


        $('.item_del_btn'+key_arr2[x]).click(function(){
        delCookie(key_arr1[x]);
    
        $('.block_'+key_arr2[x]).remove();



        var inputString = document.cookie;
        var count = (inputString.match(/=/g) || []).length; //算有幾個=符號
        console.log(count);

        if (count == 0){
            $('.have').text("購物車尚無商品!");
        }

        });

    }
 
  })


function shopcar_item(key,img,name,category,price,num,total){ 

    let html =`

        <div class="mt-2 mb-1 container-xxl block_${key}">
          <div class="row text-center  row_h align-items-center">
          
            <div class=" col-1 item_del_btn item_del_btn${key}">
                <i class="fa fa-trash" aria-hidden="true"></i>
                
            </div>
            
            <img class="img_insc col-1 "src="${img}">
            
           
            <div class="col-3 item_name1 ">${name}</div>
            <div class="col-2 item_category">${category}</div>
            <div class="col-2 item_price1">$ ${price}</div>
            <div class="col-1 item_num1">${num}</div>
            <div class="col-2 item_total1">$${total}</div>
            <hr class="mt-1 line">
          </div>
        </div>
`;

    return html;

}








//刪除cookie===============================================================

function delCookie(name)
{
   document.cookie = name+"=;expires="+(new Date(0)).toGMTString();
   
}













