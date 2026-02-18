const getCounter = async () => {
    const response = await fetch('/api');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
}

const incrementCounter = async () => {
    const response = await fetch('/api/increment', {
        method: 'POST',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
}

const decrementCounter = async () => {
    const response = await fetch('/api/decrement', {
        method: 'POST',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
}

export { getCounter, incrementCounter, decrementCounter };