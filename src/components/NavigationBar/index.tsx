import "./index.css";

function NavigationBar() {
    return (
        <nav className="NavigationBar">
            <svg viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg" className="ExpandMenuButtonIcon">
                <rect x="2" y="2" width="46" height="12" />
                <rect x="2" y="19" width="46" height="12" />
                <rect x="2" y="36" width="46" height="12" />
            </svg>
            <h2>Maze Algorithms</h2>
        </nav>
    );
}

export default NavigationBar;