import React from "react";

const Hero = () => {
  return (
    <header className='w-full flex justify-center items-center flex-col'>
      <nav className='flex justify-between items-center w-full mb-10 pt-3'>
        <span className="font-link text-slate-700 hover:text-slate-200" >#StylCheck</span>
      </nav>
      <h1 className='head_text'>
        Visual Testing at Scale <br className='max-md:hidden' />
        <span className='orange_gradient'>With CNN</span>
      </h1>
      <h3 className='desc'>
       Enter your website url to get score!
      </h3>
    </header>
  );
};

export default Hero;
