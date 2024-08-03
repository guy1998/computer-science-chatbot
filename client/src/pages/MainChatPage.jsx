import React from "react";
import "../assets/styles/main-page.css"
import PageHeader from "../components/PageHeader";
import TypeMessage from "../components/TypeMessage";
import ChatField from "../components/ChatField";
import SideBar from "../components/SideBar";
import MessageProvider from "../providers/MessageProvider";

function MainChatPage() {
    return (
        <MessageProvider>
            <div className="mainPageContainer">
                <SideBar />
                <div className="centralContainer">
                    <PageHeader />
                    <ChatField />
                    <TypeMessage />
                </div>
            </div>
        </MessageProvider>
    )
}

export default MainChatPage;