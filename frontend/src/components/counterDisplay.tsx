import { useEffect, useState } from 'react';
import { getCounter, incrementCounter, decrementCounter } from '../api/api';
import type { Counter } from '../types/counter';

const CounterDisplay = () => {
  const [counter, setCounter] = useState<Counter | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getCounter()
      .then(setCounter)
      .catch(() => setError('Failed to load counter'));
  }, []);

  const handleIncrement = () => {
    incrementCounter()
      .then(setCounter)
      .catch(() => setError('Failed to increment'));
  };

  const handleDecrement = () => {
    decrementCounter()
      .then(setCounter)
      .catch(() => setError('Failed to decrement'));
  };

  if (error) return <p>{error}</p>;
  if (!counter) return <p>Loading...</p>;

  return (
    <div>
      <p>Count: {counter.count}</p>
      <p>Times clicked: {counter.times_clicked}</p>
      <button onClick={handleDecrement}>-</button>
      <button onClick={handleIncrement}>+</button>
    </div>
  );
};

export default CounterDisplay;
