const getCounter = async () => {
    const response = await fetch('/api');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.counter;
}

const incrementCounter = async () => {
    const response = await fetch('/api/increment', {
        method: 'POST',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.counter;
}

const decrementCounter = async () => {
    const response = await fetch('/api/decrement', {
        method: 'POST',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.counter;
}

export { getCounter, incrementCounter, decrementCounter };