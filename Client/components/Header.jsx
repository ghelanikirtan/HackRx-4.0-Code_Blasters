"use client";

import { useState } from "react";
import LoginButton from "./LoginButton";
import { useSession } from "next-auth/react";
import Modal from "./Modal"

export default function Header() {
  
  const [btnPopup, setBtnPopup] = useState(false);
  const { data: session, status } = useSession();

  if (status === "authenticated") {
    return (
      <div className="flex flex-col items-center justify-center mt-5">
        <div className="text-start">
          <h1 className="text-sky-400">Welcome,
            <span className="font-bold text-2xl">{session.user.name}</span></h1>
        </div>
        <Modal/>
        {/* <button className=" border-black rounded-lg border-2 w-32 h-16 m-12 ">Create Secret Key</button> */}

        {/* <Popup trigger={btnPopup} setTrigger={setBtnPopup}>
          <h2>sfdf</h2>
        </Popup> */}
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center justify-center h-screen -mt-16">
      <h1>Login To Get Started</h1>
      <LoginButton />
    </div>
  );
}
