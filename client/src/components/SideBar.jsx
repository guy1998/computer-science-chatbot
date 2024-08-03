import React from "react";

function SideBar(){
    return(
        <div className="sideBar">
            <button className="sideBarButton" id="new"></button>
            <button className="sideBarButton" id="login"></button>
            <button className="sideBarButton" id="share"></button>
            <button className="sideBarButton" id='save'></button>
        </div>
    );
}

export default SideBar;