const lista_cores = ["red", "blue", "orange", "pink"]
let index = 0

let ultimo = -1
let atual = 0

function mundao_name(){
    setInterval(() => {
    let nomes = document.getElementsByClassName("partida");
    console.log(nomes[0], index)
    nomes[3].style.color = `${lista_cores[index]}`
    index ++
    if(index == nomes.length){
        index = 0           
        return index
    }

    }, 1000);
    
}

function um_nome_por_vez(){

    setInterval(() => {
    let nomes = document.getElementsByClassName("ordem");
    let nomes_esquerda = document.getElementsByClassName("placar_esquerda");

        
    if(atual == nomes.length){
        atual = 0;
    }
    if(ultimo >= 0){
        nomes[ultimo].style.opacity = 0;
        nomes_esquerda[ultimo].style.opacity = 0;
    }
    
    nomes[atual].style.opacity = 100;
    nomes_esquerda[atual].style.opacity = 100;
    
    ultimo = atual;
    atual ++;
    
    return ultimo, atual;}, 1000);
}

class MudarNome{

    constructor(tag){
        
        this.nomes = document.getElementsByClassName(tag);
        this.atual = 0;
        this.ultimo = -1;
        this.reset = false;
    };

    
    mudar_nome(){
        if(this.atual == this.nomes.length){

            if (this.reset){
                document.location.reload()
            }
            
            this.nomes[this.ultimo].style.opacity = 0
            this.reset = true;
            return;
            
        }
        if(this.ultimo >= 0){
            this.nomes[this.ultimo].style.opacity = 0;
            
        }
        
        this.nomes[this.atual].style.opacity = 100;
        
        
        this.ultimo = this.atual;
        this.atual ++;
        
        return this.ultimo, this.atual;
    }
}

const direita = new MudarNome("ordem")
const esqurda = new MudarNome("placar_esquerda")


function mudar_all(tag, time){
    const lado = new MudarNome(tag);
    lado.mudar_nome();
    setInterval(() => {
        lado.mudar_nome();
    }, time) 
};

function FitText(box, target_) {
    let txt = document.getElementsByClassName(target_);
    let body = document.getElementsByClassName(box);
    
    for(let i = 0; i < body.length; i++){
      let scalex_ = 1
      let target__ = txt[i].getBoundingClientRect();
      let element_ = body[i].getBoundingClientRect();
      let incial_left = element_.left
    //   console.log(body[i].textContent, incial_left)
      if(i % 2 == 0){
        body[i].style.transformOrigin  = `Right`
        
      }
      else{
        body[i].style.transformOrigin  = `Left`
      }
      while(scalex_ > 0){

          body[i].style.transform = `ScaleX(${scalex_})`
          scalex_ -= 0.01
          target__ = txt[i].getBoundingClientRect();
          element_ = body[i].getBoundingClientRect();
        //   console.log(target__, element_)
        //   console.log(target__.width, element_.width , scalex_)

          if(target__.width > element_.width){

                // console.log(element_.right, target__.right, element_.left, target__.left)
                    
                break
          }   
      }
  }    
}

function tt(){
    setInterval(() => {
        let txt = document.querySelectorAll(".txt");
        let element_ = txt[0].getBoundingClientRect();
        let element_1 = txt[1].getBoundingClientRect();
        
        console.log(element_, element_1)
    }, 2000)

}

function fitround(box, target_) {
    let txt = document.getElementsByClassName(target_);
    let body = document.getElementsByClassName(box);
    // console.log(body)
    // let rect = txt.getBoundingClientRect();
    // let rect2 = body.getBoundingClientRect();
    // let sair = (rect.width/rect2.width)*100+10
    
    for(let i = 0; i < body.length; i++){
      let scalex_ = 1
      let target__ = txt[i].getBoundingClientRect();
      let element_ = body[i].getBoundingClientRect();
    // console.log(body[i].textContent, target__.width ,  element_.width)
      while(scalex_ > 0){
        if(target__.width > element_.width){
            // console.log("AAR")
              break
          }
          body[i].style.transform = `ScaleX(${scalex_})`
          scalex_ -= 0.01
          target__ = txt[i].getBoundingClientRect();
          element_ = body[i].getBoundingClientRect();
          
        
          

      }
  };
};

function limite_name(){
    let txt = document.getElementsByClassName("txt");
    for (let h = 0; h < txt.length; h++){
        if(txt[h].textContent.length > 25){
            txt[h].textContent = `${txt[h].textContent.slice(0, 22)}...`;
        }

    }

};


limite_name();
// FitText("txt", "nome");
fitround("txt", "name");
fitround("txt_round", "round");
// fitround("txt_score", "score");
