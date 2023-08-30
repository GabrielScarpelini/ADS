import React from "react";
import { Button } from 'reactstrap';
import Headers from "./Headers";
import Article from "./Artilcle";
import Footer from "./Footer";

function App (props){
  return(
    <div>
      <Headers />
      <Article />
      <Footer />
      <Button color="danger">Danger!</Button>
    </div>
  )
};

export default App;
