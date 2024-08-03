import React, { useContext } from "react";
import MessageCloud from "./MessageCloud";
import { MessageContext } from "../providers/MessageProvider";

function ChatField(){

    const { messages } = useContext(MessageContext);

    return(
        <div className="chatField">
            {
                messages.length ? messages.map(message=>{
                    return <MessageCloud text={message.text} type={message.type}/>
                }) : <></>
            }
        </div>
    )
}

export default ChatField;