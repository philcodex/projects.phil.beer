// ==============================
// Incident Response Dashboard
// Full Working Version
// ==============================


let alertsData = [];


// ==============================
// Load Alerts
// ==============================

fetch("data/alerts.json")
.then(response => response.json())
.then(data => {

    alertsData = data;

    renderAlerts();
    updateCounters();

});



// ==============================
// Render Alerts
// ==============================

function renderAlerts() {

    const container =
        document.getElementById("alerts");

    container.innerHTML = "";

    alertsData.forEach(alert => {

        const div =
            document.createElement("div");

        // Severity colour logic

        if (alert.status === "Resolved") {

            div.className =
                "alert RESOLVED";

        }

        else {

            div.className =
                "alert " + alert.severity;

        }

        div.innerHTML = `

            <strong>${alert.severity}</strong>
            — ${alert.title}

            <br>

            Time: ${alert.time}

            <br>

            Status:
            <strong>${alert.status}</strong>

            <br><br>

            <button onclick="acknowledge(${alert.id}); event.stopPropagation();">
                Acknowledge
            </button>

            <button onclick="investigate(${alert.id}); event.stopPropagation();">
                Investigating
            </button>

            <button onclick="resolveIncident(${alert.id}); event.stopPropagation();">
                Resolve
            </button>

        `;

        // Click loads logs + timeline

        div.onclick = () => {

            loadLogs(alert.id);
            loadTimeline(alert.id);

        };

        container.appendChild(div);

    });

}



// ==============================
// Update Counters
// ==============================

function updateCounters() {

    const activeCount =
        alertsData.filter(a =>
            a.status !== "Resolved"
        ).length;

    const resolvedCount =
        alertsData.filter(a =>
            a.status === "Resolved"
        ).length;

    document.getElementById("activeCount")
        .innerText = activeCount;

    document.getElementById("resolvedCount")
        .innerText = resolvedCount;

}



// ==============================
// Status Actions
// ==============================

function acknowledge(id) {

    updateStatus(id, "Acknowledged");

}

function investigate(id) {

    updateStatus(id, "Investigating");

}

function resolveIncident(id) {

    updateStatus(id, "Resolved");

}



// ==============================
// Update Status + Timeline
// ==============================

function updateStatus(id, status) {

    alertsData.forEach(alert => {

        if (alert.id === id) {

            alert.status = status;

            const time =
                new Date()
                .toLocaleTimeString();

            if (!alert.timeline) {

                alert.timeline = [];

            }

            alert.timeline.push(
                time + " — Status: " + status
            );

        }

    });

    renderAlerts();
    updateCounters();
    loadTimeline(id);

}



// ==============================
// Load Logs
// ==============================

function loadLogs(id) {

    fetch("logs/sample-logs.txt")

    .then(response => response.text())

    .then(data => {

        const logViewer =
            document.getElementById("logs");

        logViewer.textContent =

            "Incident ID: " + id +

            "\n\n" +

            data;

    });

}



// ==============================
// Load Timeline
// ==============================

function loadTimeline(id) {

    const incident =
        alertsData.find(a =>
            a.id === id
        );

    const timelineDiv =
        document.getElementById("timeline");

    timelineDiv.innerHTML = "";

    if (!incident ||
        !incident.timeline ||
        incident.timeline.length === 0) {

        timelineDiv.innerHTML =
            "<p>No timeline available</p>";

        return;

    }

    incident.timeline.forEach(event => {

        const p =
            document.createElement("p");

        p.textContent = event;

        timelineDiv.appendChild(p);

    });

}



// ==============================
// Simulated Alert Generator
// ==============================

const incidentTypes = [

"API Latency > 500ms",
"TLS Certificate Expiring",
"Disk Usage > 85%",
"Unauthorized Login Attempt",
"High Memory Usage",
"Database Failover Triggered"

];

function generateRandomAlert() {

    const newId =
        alertsData.length + 1;

    const randomTitle =
        incidentTypes[
            Math.floor(
                Math.random() *
                incidentTypes.length
            )
        ];

    const newAlert = {

        id: newId,

        severity: randomSeverity(),

        title: randomTitle,

        time:
            new Date()
            .toLocaleTimeString(),

        status: "Active",

        timeline: [

            new Date()
            .toLocaleTimeString() +
            " — Alert Triggered"

        ]

    };

    alertsData.unshift(newAlert);

    renderAlerts();
    updateCounters();

}



// ==============================
// Random Severity
// ==============================

function randomSeverity() {

    const levels = [

        "CRITICAL",
        "HIGH",
        "MEDIUM"

    ];

    return levels[

        Math.floor(
            Math.random() *
            levels.length
        )

    ];

}



// Auto-generate alerts every 30 seconds

setInterval(
    generateRandomAlert,
    30000
);



// ==============================
// Live Clock
// ==============================

setInterval(() => {

    const clock =
        document.getElementById("clock");

    if (clock) {

        clock.innerText =
            new Date()
            .toLocaleTimeString();

    }

}, 1000);



// ==============================
// Notes Persistence
// ==============================

window.onload = () => {

    const notesField =
        document.getElementById("notes");

    if (notesField) {

        notesField.value =
            localStorage.getItem("incidentNotes")
            || "";

        notesField.addEventListener("input", () => {

            localStorage.setItem(
                "incidentNotes",
                notesField.value
            );

        });

    }

};