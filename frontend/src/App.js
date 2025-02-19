import React from 'react';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>AI-powered Resume Analyzer</h1>
      </header>
      <main>
        <form>
          <label>
            Upload your resume:
            <input type="file" name="resume" />
          </label>
          <button type="submit">Analyze</button>
        </form>
      </main>
    </div>
  );
}

export default App;
