'use client';

import React from 'react';
import { motion } from 'framer-motion';

const Hero = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="container mx-auto px-6 text-center">
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="text-4xl md:text-6xl font-bold text-black mb-6 leading-tight"
        >
          Shopping has never been easier. Use your <span className='bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-indigo-600'>voice</span> to buy your favourite products.
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="text-lg md:text-xl text-gray-600 mb-10 max-w-3xl mx-auto"
        >
          Meet Wally - your personal AI shopping assistant. Just say what you need, and we'll handle the rest.
        </motion.p>
        <motion.button
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5, delay: 0.6 }}
          whileHover={{ scale: 1.05, boxShadow: '0px 10px 30px rgba(99, 102, 241, 0.5)' }}
          whileTap={{ scale: 0.95 }}
          className="bg-gradient-to-r from-blue-500 to-purple-600 text-white font-bold py-4 px-10 rounded-full text-lg shadow-lg"
        >
          Get Started
        </motion.button>
      </div>
    </div>
  );
};

export default Hero;