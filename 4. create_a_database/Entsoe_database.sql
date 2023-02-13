CREATE TABLE IF NOT EXISTS Load (
  id serial primary key,
  country VARCHAR(20) not null,
  time timestamp not null,
  actual_load NUMERIC(8,2),
  forecast_load NUMERIC(8,2)
);

CREATE TABLE IF NOT EXISTS Generation(
  id serial primary key,
  country VARCHAR(20) not null,
  time timestamp not null,
  actual_generation NUMERIC(8,2),
  forecast_generation NUMERIC(8,2)
);