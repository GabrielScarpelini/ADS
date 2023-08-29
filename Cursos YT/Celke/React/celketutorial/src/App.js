import React from "react";
import { Button } from 'reactstrap';
import Headers from "./Headers";
import Article from "./Article";
import Footer from "./Footer";
// function App() {
//   return (
//     <div className="App">
//       Olá Gabriel
//     </div>
//   );
// }


function App (props) {
  return (
    <div>
      <Headers />
      <Article />
      <Footer />
      <Button color="danger">Danger!</Button>
    </div>
  )
};

export default App;
