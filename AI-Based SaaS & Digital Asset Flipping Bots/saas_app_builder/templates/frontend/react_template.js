import React, { useState } from 'react';

function App() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async () => {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ input }),
    });
    const data = await response.json();
    setResult(data.prediction);
  };

  return (
    <div>
      <h1>{{ app_name }}</h1>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={handleSubmit}>Predict</button>
      <p>Result: {result}</p>
    </div>
  );
}

export default App;