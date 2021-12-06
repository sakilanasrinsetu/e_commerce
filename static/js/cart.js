console.log("Connected.....")
var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'action:',action)
        
        console.log('USER:'.user)
        if (user == 'AnonymousUser'){
            alert("User is Not Authenticated")
        }else{
            console.log("User is authenticated, sending data ... ")
        }
    })
}
