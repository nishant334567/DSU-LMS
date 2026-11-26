export function Card({ children, className = "" }) {
  return <section className={`card ${className}`}>{children}</section>;
}

export function SectionHeader({ eyebrow, title, description, aside }) {
  return (
    <div className="section-header">
      <div>
        {eyebrow && <p className="eyebrow">{eyebrow}</p>}
        <h2>{title}</h2>
        {description && <p className="section-description">{description}</p>}
      </div>
      {aside}
    </div>
  );
}

export function Badge({ children }) {
  return <span className="badge">{children}</span>;
}

export function Stat({ label, value, detail, icon }) {
  return (
    <Card className="stat-card">
      <div className="stat-top">
        <span className="stat-label">{label}</span>
        <span className="stat-icon" aria-hidden="true">{icon}</span>
      </div>
      <strong className="stat-value">{value}</strong>
      <span className="stat-detail">{detail}</span>
    </Card>
  );
}

export function EmptyState({ children }) {
  return <p className="empty-state">{children}</p>;
}

export function LoadingState() {
  return (
    <div className="notice" role="status">
      <span className="spinner" aria-hidden="true" />
      Loading your learning dashboard…
    </div>
  );
}
