import NavigationBar from "./components/NavigationBar";
import { useRef, MutableRefObject } from "react";
import "./App.css";

function App() {
    const canvas: MutableRefObject<null | HTMLCanvasElement> = useRef(null);

    return (
        <div className="App">
            <NavigationBar />
            <canvas ref={canvas} />
        </div>
    );
}

export default App;