import React from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

const Home = () => {
  return (
    <div>
      <Navbar />
      <main>
        <h1>Welcome to DeArbi Network</h1>
        <p>Your gateway to decentralized arbitrage.</p>
      </main>
      <Footer />
    </div>
  );
};

export default Home;
