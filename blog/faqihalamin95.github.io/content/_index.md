---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      headings:
        about: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '📚 My Learning & Projects'
      subtitle: ''
      text: |-
        I document my journey toward becoming a Data Engineer by building hands-on projects that mirror real-world challenges. My focus areas include:

        - Designing ETL pipelines with Python and SQL.
        - Cleaning, transforming, and normalizing messy datasets.
        - Implementing reproducible workflows and data versioning.
        - Exploring scalable tools like Polars, Databricks, and cloud-based data storage.
        
        I share insights, lessons, and practical examples from each stage of my roadmap in data engineering expertise. 
    design:
      columns: '1'
  - block: collection
    content:
      title: Pinned Post
      filters:
        folders:
          - blog
        featured_only: true
    design:
      view: showcase
      columns: '1'
  - block: collection
    content:
      title: Blog Posts
      text: ''
      filters:
        folders:
          - blog
        exclude_featured: true
      count: '2'
      order: desc
    design:
      view: article-grid
      columns: '2'
  # - block: collection
  #   content:
  #     title: Projects
  #     filters:
  #       folders:
  #         - projects
  #     count: '1'
  #     order: desc
  #   design:
  #     view: article-grid
  #     columns: '1'
---
