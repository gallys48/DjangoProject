let point = document.querySelectorAll('.point')
let imageSlider = document.querySelectorAll('.imageSlider')
let Prev = document.getElementById('Prev')
let Next = document.getElementById('Next')

point[0].classList.add('activeImage')
imageSlider[0].classList.add('activeImage')

let counter = 0;

for(let i=0; i<point.length; i++){
  point[i].addEventListener('click',()=>{
    for(let k = 0; k<imageSlider.length; k++){
      point[k].classList.remove('activeImage')
      imageSlider[k].classList.remove('activeImage')
    }
    counter = i;
    imageSlider[counter].classList.add('activeImage')
    point[counter].classList.add('activeImage')
  })
}

Prev.addEventListener('click',()=>{
  for(let k = 0; k<imageSlider.length; k++){
    point[k].classList.remove('activeImage')
    imageSlider[k].classList.remove('activeImage')
  }
  counter--
  if (counter<0){
    counter = imageSlider.length-1
  }
  imageSlider[counter].classList.add('activeImage');
  point[counter].classList.add('activeImage');
})

Next.addEventListener('click',()=>{
  for(let k = 0; k<imageSlider.length; k++){
    point[k].classList.remove('activeImage')
    imageSlider[k].classList.remove('activeImage')
  }
  counter++
  if (counter>= imageSlider.length){
    counter = 0
  }
  imageSlider[counter].classList.add('activeImage');
  point[counter].classList.add('activeImage');
})

function slowSlider() {
  for(let k = 0; k<imageSlider.length; k++){
    point[k].classList.remove('activeImage')
    imageSlider[k].classList.remove('activeImage')
  }
  counter++
  if (counter>= imageSlider.length){
    counter = 0
  }
  imageSlider[counter].classList.add('activeImage');
  point[counter].classList.add('activeImage');
}

let second = 1000*4
let TimerImage = setInterval(()=>slowSlider(), second )

let blockSlider = document.getElementById('blockSlider')
blockSlider.addEventListener('mouseover',()=>{
  clearInterval(TimerImage)
})

blockSlider.addEventListener('mouseleave',()=>{
  TimerImage = setInterval(()=>slowSlider(), second )
})

