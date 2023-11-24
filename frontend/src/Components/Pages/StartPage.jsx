import "./StartPage.css";

const StarLocation = (x, y) => {
  return x + Math.random() * (y - x);
};
//var style = `top: ${StarLocation(0, 100)}%; left: ${StarLocation(0, 100)}%;`;

const setLocation = () => {
  for (var i = 0; i < 100; i++) {
    document.body.innerHTML += '<div className="star" style="top: ' + StarLocation(0, 100) + 
    '%; left: ' + StarLocation(0, 100) + '%;"></div>'
  }
  console.log('done');
}

export const StartPage = () => {
  setLocation();
  return(
    <div>
      Hello
    </div>
  )
};
  
  
