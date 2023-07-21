import React, { useState } from "react";
// import "./Modal.css";

export default function Modal() {
  const [modal, setModal] = useState(false);
  const [key,setKey]= useState(null);

  const toggleModal = () => {
    setModal(!modal);
  };

  if(modal) {
    document.body.classList.add('active-modal')
  } else {
    document.body.classList.remove('active-modal')
  }

  function submit(e){
    e.preventDefault(); 
    //api call
    const key="key1";
    setKey(key);
  }

  return (
    <>
      <button onClick={toggleModal} className="border-black rounded-lg border-2 w-32 text-14 mt-12">
        Create Secret Key
      </button>

      {modal && (
        <div className="modal">
          <div onClick={toggleModal} className="overlay"></div>
          <div className="bg-slate-100 rounded-lg w-auto
           h-52 mt-12 p-3">
            <form onSubmit={submit}>
                <input type="text" placeholder="Enter name for key"className="border-black rounded-lg border-2 p-2"/>
                <button className="border-black rounded-lg border-2 w-auto h-12 m-2 p-2 bg-green-400">Generate Key</button>
            </form>
            <div className="response">
                {key && <p>{key}</p>}
            </div>
            {/* <button className="close-modal justify-items-end" onClick={toggleModal}>
              X
            </button> */}
            
          </div>
        </div>
      )}
    </>
  );
}