import logo from './logo.svg';
import './App.css';
import Texto from "./Texto"


  function App() {
	function showMessage(){
		alert("Salve mundão")
	  }
  return (
    <div className="App">
      <header className="App-header">
	
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
		<button onClick={showMessage}>Botão salve</button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
