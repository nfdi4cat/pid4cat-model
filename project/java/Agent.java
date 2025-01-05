package None;

import java.util.List;
import lombok.*;






/**
  Person who plays a role relative to PID creation or curation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Agent  {

  private String name;
  private String email;
  private String orcid;
  private String affiliationRor;
  private String role;

}