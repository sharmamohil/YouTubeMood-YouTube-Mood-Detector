// Home.js
import React, { useState } from 'react';
import MoodDashboard from './MoodDashboard';

const Home = () => {
  const [isConnected, setIsConnected] = useState(false);

  const handleConnect = () => {
    // Mock connection logic
    setIsConnected(true);
  };

  return (
    <div className="home">
      <header className="hero">
        <h2>Discover Your Mood from Your YouTube Shorts</h2>
        <p>Let your favorite Shorts reflect your mood.</p>
        <button className="connect-button" onClick={handleConnect}>
          {isConnected ? 'Connected' : 'Connect Your YouTube'}
        </button>
      </header>

      <section className="features">
        <h3>Why Use YouTubeMood?</h3>
        <div className="feature-cards">
          <div className="feature-card">
            <h4>Real-Time Mood Analysis</h4>
            <p>Understand your mood based on the content of your YouTube Shorts.</p>
          </div>
          <div className="feature-card">
            <h4>Video and Audio Insights</h4>
            <p>Analyze both visual and auditory content for an accurate mood reading.</p>
          </div>
          <div className="feature-card">
            <h4>Privacy Protection</h4>
            <p>We securely analyze your data and ensure full privacy.</p>
          </div>
        </div>
      </section>

      <section className="how-it-works">
        <h3>How It Works</h3>
        <div className="steps">
          <div className="step">
            <h4>1. Connect to YouTube</h4>
            <p>Sign in with your YouTube account to allow access to your Shorts.</p>
          </div>
          <div className="step">
            <h4>2. Analyze Content</h4>
            <p>We extract and analyze your Shorts' titles, descriptions, and comments.</p>
          </div>
          <div className="step">
            <h4>3. Get Mood Insights</h4>
            <p>See your mood trends based on your YouTube activity.</p>
          </div>
        </div>
      </section>

      <section className="dashboard">
        <h3>Your Mood Dashboard</h3>
        {isConnected ? <MoodDashboard /> : <p>Connect your YouTube account to see your mood analysis!</p>}
      </section>
    </div>
  );
};

export default Home;
