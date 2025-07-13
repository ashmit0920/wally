'use client';

import React from 'react';
import { motion } from 'framer-motion';

const products = [
  {
    id: 1,
    name: 'Wireless Headphones',
    description: 'Immersive sound quality with noise cancellation.',
    price: '$99.99',
    image: 'https://source.unsplash.com/random/400x400?headphones'
  },
  {
    id: 2,
    name: 'Smartwatch',
    description: 'Stay connected and track your fitness goals.',
    price: '$199.99',
    image: 'https://source.unsplash.com/random/400x400?smartwatch'
  },
  {
    id: 3,
    name: 'Coffee Maker',
    description: 'Brew the perfect cup of coffee every morning.',
    price: '$49.99',
    image: 'https://source.unsplash.com/random/400x400?coffeemaker'
  },
  {
    id: 4,
    name: 'Running Shoes',
    description: 'Lightweight and comfortable for your daily run.',
    price: '$129.99',
    image: 'https://source.unsplash.com/random/400x400?runningshoes'
  },
  {
    id: 5,
    name: 'Blender',
    description: 'Create delicious smoothies and shakes with ease.',
    price: '$79.99',
    image: 'https://source.unsplash.com/random/400x400?blender'
  },
  {
    id: 6,
    name: 'Yoga Mat',
    description: 'High-quality, non-slip mat for your yoga practice.',
    price: '$29.99',
    image: 'https://source.unsplash.com/random/400x400?yogamat'
  }
];

const Products = () => {
  return (
    <div className="min-h-screen bg-gray-100 py-20">
      <div className="container mx-auto px-6">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-4xl font-bold text-center text-gray-800 mb-16"
        >
          Our Products
        </motion.h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
          {products.map((product, index) => (
            <motion.div
              key={product.id}
              className="bg-white rounded-2xl shadow-lg overflow-hidden"
              initial={{ opacity: 0, y: 50, scale: 0.9 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              whileHover={{ scale: 1.05, y: -10, boxShadow: '0px 20px 40px rgba(0, 0, 0, 0.1)' }}
            >
              <img src={product.image} alt={product.name} className="w-full h-64 object-cover" />
              <div className="p-6">
                <h3 className="text-2xl font-bold text-gray-800 mb-2">{product.name}</h3>
                <p className="text-gray-600 mb-4">{product.description}</p>
                <div className="flex justify-between items-center">
                  <p className="text-2xl font-bold text-blue-500">{product.price}</p>
                  <button className="bg-gradient-to-r from-blue-500 to-purple-600 text-white font-bold py-2 px-5 rounded-full shadow-md">Add to Cart</button>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Products;