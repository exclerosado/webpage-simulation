window.addEventListener('load', setup);

async function setup(){
    const datas = await getData();
    const ctx = document.getElementById('chart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: datas.names,
            datasets: [{
                data: datas.values,
                fill: false,
                backgroundColor: [
                    'rgb(54, 160, 235)',
                    'rgb(255, 99, 130)',
                    'rgb(255, 159, 65)',
                    'rgb(255, 205, 85)',
                    'rgb(75, 192, 190)'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Funnel Pageviews'
                }
            }
        }
    });
};

async function getData(){
    const response = await fetch('data.csv');
    const data = await response.text();
    const names = [];
    const values = [];
    const rows = data.split('\n');
    
    rows.forEach(row => {
        const cols = row.split(',');
        names.push(cols[0]);
        values.push(cols[1])
    });
    return { names, values };
};