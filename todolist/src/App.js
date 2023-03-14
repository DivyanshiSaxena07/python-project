import logo from './logo.svg';
import './App.css';
import TodoList from './components/TodoList';

function App() {
  return (
    <div className="App">
     <div className="container" style={{backgroundColor:'whiteSmoke',borderRadius: "10px "}}>
      <h1 style={{backgroundColor:"#FF9999"}} className="button button2">TodoList</h1>
      <TodoList/>
     </div>
    </div>
  );
}

export default App;
