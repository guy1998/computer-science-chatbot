import React, { createContext, useState } from "react";

export const MessageContext = createContext();

function MessageProvider(props){

    const [messages, setMessages] = useState([]);

    return (
        <MessageContext.Provider value={{ messages, setMessages }}>
            { props.children }
        </MessageContext.Provider>
    )

}

export default MessageProvider;