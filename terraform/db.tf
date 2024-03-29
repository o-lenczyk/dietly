resource "google_sql_database" "database" {
  name     = "dietly"
  instance = google_sql_database_instance.instance.name
}

# See versions at https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#database_version
resource "google_sql_database_instance" "instance" {
  name             = "database-instance"
  region           = local.location
  database_version = "POSTGRES_15"
  settings {
    tier = "db-f1-micro"
  }
  deletion_protection  = "false"
}

resource "google_sql_user" "users" {
  name     = "orest"
  instance = google_sql_database_instance.instance.name
  password = "changeme"
}

resource "google_sql_user" "iam_service_account_user" {
  # Note: for Postgres only, GCP requires omitting the ".gserviceaccount.com" suffix
  # from the service account email due to length limits on database usernames.
  name     = replace(data.google_client_openid_userinfo.me.email, ".gserviceaccount.com", "")
  instance = google_sql_database_instance.instance.name
  type     = "CLOUD_IAM_SERVICE_ACCOUNT"
}

data "google_client_openid_userinfo" "me" {}


resource "google_sql_ssl_cert" "client_cert" {
  common_name = "client-name"
  instance    = google_sql_database_instance.instance.name
}