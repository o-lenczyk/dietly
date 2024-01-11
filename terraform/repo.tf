resource "google_artifact_registry_repository" "my-repo" {
  location      = local.location
  repository_id = "dietly"
  format        = "DOCKER"

  docker_config {
    immutable_tags = false
  }
}

resource "google_service_account" "repo-account" {
  account_id   = "dietly-repo-admin"
  display_name = "Repository Service Account"
}

resource "google_artifact_registry_repository_iam_member" "repo-iam" {
  location = google_artifact_registry_repository.my-repo.location
  repository = google_artifact_registry_repository.my-repo.name
  role   = "roles/artifactregistry.repoAdmin"
  member = "serviceAccount:${google_service_account.repo-account.email}"
}
