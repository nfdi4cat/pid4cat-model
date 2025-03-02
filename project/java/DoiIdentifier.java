package None;

import java.util.List;
import lombok.*;






/**
  A digital object identifier (DOI).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DoiIdentifier extends RelatedIdentifier {

  private String resolvingUrl;
  private String identifier;

}
