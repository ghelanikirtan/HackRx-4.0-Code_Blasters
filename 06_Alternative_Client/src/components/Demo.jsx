import React, { useState, useEffect } from "react";
import { copy, linkIcon, loader, tick } from "../assets";

const Demo = () => {
  const [websiteURL, setWebsiteURL] = useState('');
  const [responseData, setResponseData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('https://4467-103-68-38-66.ngrok-free.app/test-it-up', {
        mode: 'cors',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: websiteURL }),
      });

      if (response.ok) {
        console.log('fs');
        const data = await response.json();
        setResponseData(data);
        console.log('Response received:', data);
      } else {
        console.error('Failed to get response');
        // Handle errors or show error message
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  // copy the url and toggle the icon for user feedback
  const handleCopy = (copyUrl) => {
    setCopied(copyUrl);
    navigator.clipboard.writeText(copyUrl);
    setTimeout(() => setCopied(false), 3000);
  };

  const handleKeyDown = (e) => {
    if (e.keyCode === 13) {
      handleSubmit(e);
    }
  };

  return (
    <section className='mt-16 w-full max-w-xl'>
      <div className='flex flex-col w-full gap-2'>
        <form onSubmit={handleSubmit} className='relative flex justify-center items-center'>
          <img        // copy icon
            src={linkIcon}
            alt='link-icon'
            className='absolute left-0 my-2 ml-3 w-5'
          />
          <input
            placeholder="Enter your website url"
            className='url_input peer'
            value={websiteURL} type="text"
            onChange={(e) => setWebsiteURL(e.target.value)}
          />
          <button type="submit" className='submit_btn peer-focus:border-gray-700 peer-focus:text-gray-700  hover:bg-slate-100 '>
            <p>↵</p>
          </button>
        </form>

      </div>

    </section>
  );
};

export default Demo;
