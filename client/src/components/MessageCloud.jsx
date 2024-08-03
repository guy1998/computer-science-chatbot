import React from "react";
import "../assets/styles/main-page.css"

function MessageCloud({ text, type }) {
    return (
        <div className="aligner" style={{ justifyContent: type === 'answer' ? 'start' : 'end'}}>
            <div className={"messageCloud " + type}>
                <p>{text}</p>
            </div>
        </div>
    )
}

export default MessageCloud;